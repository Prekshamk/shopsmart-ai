export default function FeatureCard({ title, description }) {
  return (
    <div
      style={{
        backgroundColor: '#ffffff',
        padding: '32px',
        borderRadius: '20px',
        width: '300px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
        textAlign: 'center',
      }}
    >
      <h3 style={{ marginBottom: '16px', color: '#111827' }}>{title}</h3>
      <p style={{ color: '#4b5563', lineHeight: '1.6' }}>{description}</p>
    </div>
  );
}