from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def home():
    return "🟢 YouTube Transcript API está no ar!"

@app.route('/transcript', methods=['POST'])
def transcript():
    data = request.get_json()
    video_id = data.get('videoId')
    if not video_id:
        return jsonify({"error": "Parâmetro 'videoId' é obrigatório"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([x['text'] for x in transcript])
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
