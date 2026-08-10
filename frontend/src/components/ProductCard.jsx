export default function ProductCard({ name, price, image, onAddToCart }) {
  return (
    <div
      style={{
        backgroundColor: '#ffffff',
        borderRadius: '18px',
        padding: '20px',
        width: '260px',
        boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
        textAlign: 'center',
      }}
    >
      <img
        src={image}
        alt={name}
        style={{
          width: '100%',
          height: '180px',
          objectFit: 'cover',
          borderRadius: '12px',
          marginBottom: '16px',
        }}
      />

      <h3 style={{ marginBottom: '8px', color: '#111827' }}>{name}</h3>

      <p style={{ fontSize: '20px', fontWeight: 'bold', color: '#2563eb' }}>
        ₹{price}
      </p>

      <button
  onClick={onAddToCart}
  style={{
    backgroundColor: '#2563eb',
    color: '#fff',
    border: 'none',
    borderRadius: '10px',
    padding: '10px 20px',
    cursor: 'pointer',
    fontWeight: '600'
  }}
>
  Add to Cart
</button>
    </div>
  );
}