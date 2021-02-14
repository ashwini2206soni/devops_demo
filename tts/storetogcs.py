from google.cloud import storage

def store_audio_to_gcs(audio_bytes,bucket_name="demo_bucket_1_testing"):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("demo_bucket_1_testing")
    blob = bucket.blob("AudioFile.mp3")
    blob.upload_from_string(audio_bytes,content_type="audio/mpeg")
    return "Audio file saved to GCS bucket: "+ "demo_bucket_1_testing"+"under name: AudioFile.mp3"