print("=== AI Trend Agent ===")

topic = input("Kis topic par research karni hai? : ")

videos = [
    "Top 10 " + topic + " Tips",
    topic + " Explained",
    "Best " + topic + " Tricks",
    topic + " for Beginners",
    topic + " Secrets"
]

print("\nTrending Videos:\n")print(f"{i}. {video}")
for i, video in enumerate(videos, start=1):
    print(f"{i}. {video}"
