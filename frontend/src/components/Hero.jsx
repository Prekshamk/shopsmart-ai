export default function Hero() {
  return (
    <section
      style={{
        textAlign: 'center',
        padding: '100px 20px',
      }}
    >
      <h1
        style={{
          fontSize: '56px',
          color: '#111827',
          marginBottom: '20px',
        }}
      >
        Shop Smarter with AI
      </h1>

      <p
        style={{
          fontSize: '22px',
          color: '#4b5563',
          maxWidth: '850px',
          margin: '0 auto 40px',
          lineHeight: '1.6',
        }}
      >
        Personalized product recommendations, smart price comparison, and
        sustainable shopping choices powered by artificial intelligence.
      </p>

      <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', flexWrap: 'wrap' }}>
        <button
          style={{
            padding: '14px 28px',
            borderRadius: '12px',
            border: 'none',
            backgroundColor: '#2563eb',
            color: '#ffffff',
            fontSize: '18px',
            cursor: 'pointer',
          }}
        >
          Start Shopping
        </button>

        <button
          style={{
            padding: '14px 28px',
            borderRadius: '12px',
            border: '2px solid #2563eb',
            backgroundColor: '#ffffff',
            color: '#2563eb',
            fontSize: '18px',
            cursor: 'pointer',
          }}
        >
          Ask AI Assistant
        </button>
      </div>
    </section>
  );
}