# Zero-shot = give the task directly, no examples. The model uses only what it learned during training.
from openai import OpenAI

MODEL = "phi3:mini"    # 4 GB RAM
# MODEL = "gemma2:2b"  # 8 GB RAM

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

prompt = """Been using the Cosmic Byte Blitz 
Tri Mode for a few weeks now and honestly didn't expect 
this much from a budget controller. Build quality feels solid,
 buttons have a satisfying click, and the tri-mode connectivity 
 (Bluetooth, 2.4GHz, wired) works flawlessly. Connected to my PC via USB and it was plug-and-play —
 zero driver headaches. Latency is noticeably low in wired mode,
   great for fast-paced games. Battery life is decent too. Thumbsticks feel smooth, no stick drift so far. RGB lighting is a nice touch. If you're looking for a reliable PC/Android controller under ₹2000, this is easily one of the best options out there. Highly recommend

Review: "The camera quality is great but the battery drains too fast." """

r = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=5,
    temperature=0.0,   # deterministic — classification should always give the same answer
)
print(r.choices[0].message.content.strip())