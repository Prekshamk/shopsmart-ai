import { useState } from 'react';

export default function AIAssistant() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState(
    'Hi! Ask me for product recommendations.'
  );

  const handleAsk = () => {
    if (!question.trim()) return;

    if (question.toLowerCase().includes('headphone')) {
      setResponse('I recommend the Wireless Headphones for music and calls.');
    } else if (question.toLowerCase().includes('watch')) {
      setResponse('The Smart Watch is great for fitness tracking and notifications.');
    } else if (question.toLowerCase().includes('eco')) {
      setResponse('Choose the Eco Water Bottle for a sustainable lifestyle.');
    } else {
      setResponse('I can help you choose headphones, watches, or eco products.');
    }
  };

  return (
    <section
      style={{
        backgroundColor: '#ffffff',
        margin: '40px auto',
        padding: '30px',
        borderRadius: '20px',
        maxWidth: '700px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
      }}
    >
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>
        AI Shopping Assistant
      </h2>

      <div
        style={{
          backgroundColor: '#f3f4f6',
          padding: '20px',
          borderRadius: '12px',
          minHeight: '80px',
          marginBottom: '20px',
          color: '#111827',
        }}
      >
        {response}
      </div>

      <div style={{ display: 'flex', gap: '12px' }}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask for a product recommendation..."
          style={{
            flex: 1,
            padding: '12px',
            borderRadius: '10px',
            border: '1px solid #d1d5db',
            fontSize: '16px',
          }}
        />

        <button
          onClick={handleAsk}
          style={{
            padding: '12px 20px',
            borderRadius: '10px',
            border: 'none',
            backgroundColor: '#2563eb',
            color: '#ffffff',
            cursor: 'pointer',
            fontWeight: '600',
          }}
        >
          Ask AI
        </button>
      </div>
    </section>
  );
}