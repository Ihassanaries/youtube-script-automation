from fetch_topics import get_topic_and_category
from generate_script import generate_script
from save_to_docs import save_to_google_docs

def main():
    for topic, category in get_topic_and_category():
        prompt = f"Write a YouTube script for the category {category} about {topic}. Make it engaging and story-driven."
        print(f"Generating script for: {topic}")

        script = generate_script(topic, prompt)
        doc_link = save_to_google_docs(script, topic)
        print(f"✅ Script saved: {doc_link}\n")

if __name__ == "__main__":
    main()
