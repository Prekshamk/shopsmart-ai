import { useState } from 'react';

export default function AIAssistant() {
  const [input, setInput] = useState('');
  const [reply, setReply] = useState('Hi! Ask me for product recommendations.');

  const askAI = async () => {
    if (!input.trim()) return;

    try {
      const response = await fetch('http://127.0.0.1:5000/api/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });

      const data = await response.json();
      setReply(data.answer);
    } catch (error) {
      setReply('Backend not connected');
      console.error(error);
    }
  };

  return (
    <section
      style={{
        backgroundColor: '#ffffff',
        maxWidth: '900px',
        margin: '40px auto',
        padding: '30px',
        borderRadius: '20px',
        boxShadow: '0 10px 30px rgba(0,0,0,0.08)',
      }}
    >
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>
        AI Shopping Assistant
      </h2>

      <div
        style={{
          backgroundColor: '#f3f4f6',
          padding: '24px',
          borderRadius: '14px',
          minHeight: '120px',
          marginBottom: '20px',
          fontSize: '20px',
          color: '#111827',
          textAlign: 'center',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {reply}
      </div>

      <div style={{ display: 'flex', gap: '12px' }}>
        <input
          type="text"
          placeholder="Ask for headphones, watch, or bottle..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{
            flex: 1,
            padding: '16px',
            borderRadius: '12px',
            border: '1px solid #d1d5db',
            fontSize: '18px',
          }}
        />

        <button
          onClick={askAI}
          style={{
            backgroundColor: '#2563eb',
            color: '#fff',
            border: 'none',
            borderRadius: '12px',
            padding: '0 24px',
            fontSize: '18px',
            cursor: 'pointer',
          }}
        >
          Ask AI
        </button>
      </div>
    </section>
  );
}