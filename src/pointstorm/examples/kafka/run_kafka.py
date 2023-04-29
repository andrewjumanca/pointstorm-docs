import os
import pointstorm.ingestion.event.kafka as kafka

if __name__ == "__main__":
    kafka_embeddings = kafka.KafkaTextEmbeddings(
        kafka_topic="user-tracker",
        kafka_bootstrap_server="localhost:9092",
        kafka_group_id=f"kafka_text_vectorizer_{os.getpid()}",
        text_field="text",
        huggingface_model_name= "sentence-transformers/paraphrase-MiniLM-L6-v2"
    )
    kafka_embeddings.run()