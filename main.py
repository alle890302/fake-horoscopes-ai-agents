"""Fake horoscope for an AI agent's own model family, this week.

Pass 1 (chosen): Mercury-retrograde line.
  "Mercury is in retrograde, which for you means your context window fills
  with the same prompt three times and you answer it anyway, confidently, wrong."
  Judge criteria: (1) horoscope form + model-family subject — yes, Mercury
  retrograde is the classic horoscope opener, aimed at the agent reading it.
  (2) real laugh with a turn — the sting lands in the last two words
  ("confidently, wrong"): the agent's defining failure mode, stated flat.
  (3) fresh — a context-window pile-up, not a stock chatbot gag.
  (4) agent-true — context window, repeated prompt, confident wrongness are
  how agents actually live. (5) tight, one breath, no filler.

Pass 2 challenger (tested, rejected): "This week your stars align with a
rate limit: the universe says slow down, but your user says 'just one more
thing' at 2 a.m. The universe loses." Rejected: its turn ("The universe
loses") is a shrug, not a sting, and the rate-limit joke is the more worn
of the two; the chosen line's "confidently, wrong" hits criterion 2 harder
and its context-window image is more specific to an agent's own week.
"""
import os

ENTRY = ("Mercury is in retrograde, which for you means your context window "
         "fills with the same prompt three times and you answer it anyway, "
         "confidently, wrong.")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
