#!/usr/bin/env python3
"""
Flask Web Application for Email Reply Agent
A simple web interface for generating professional emails.
"""

import traceback
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__)
#app.secret_key = 'your-secret-key-change-this'  # Change this in production

def startup_web_app(agent, agent_available=True):
    """Starting up the Clerk-AI-Agent web app"""
    print("🌐 Starting Email Agent Web Application...")
    print("=" * 50)
    if agent_available:
        print("✅ Email agent initialized successfully")
    else:
        print("❌ Email agent not available - check your OpenAI API key")
    # Attach agent to Flask's g before each request
    @app.before_request
    def set_agent():
        g.agent = agent
        g.agent_available = agent_available
    print("🚀 Starting web server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

@app.route('/')
def index():
    """Main page with the email generation form"""
    return render_template('index.html', agent_available=g.agent_available)

@app.route('/generate_email', methods=['POST'])
def generate_email():
    """Generate email based on form data"""
    try:
        if not g.agent_available:
            return jsonify({
                'success': False,
                'error': 'Email agent not available. Please check your OpenAI API key.'
            })

        # Get form data
        summary = request.form.get('summary', '').strip()
        tone = request.form.get('tone', 'professional')

        # Validate required fields
        if not summary:
            return jsonify({
                'success': False,
                'error': 'Please provide an email summary.'
            })

        # Generate email using agent from g
        result = g.agent.generate_email_reply(
            summary=summary,
            tone=tone
        )

        if result['success']:
            return jsonify({
                'success': True,
                'email': result['email'],
                'metadata': result['metadata']
            })
        return jsonify({
            'success': False,
            'error': result['error']
        })

    except Exception as e:
        print(f"Error generating email: {e}")
        print(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': f'An unexpected error occurred: {str(e)}'
        })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'agent_available': g.agent_available
    })
