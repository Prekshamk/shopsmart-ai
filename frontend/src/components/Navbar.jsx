export default function Navbar({ cartCount, onCartClick }) {
  return (
    <nav
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '20px 40px',
        backgroundColor: '#ffffff',
        borderBottom: '1px solid #e5e7eb',
      }}
    >
      <h2 style={{ color: '#1e3a8a' }}>ShopSmart AI</h2>

      <div style={{ display: 'flex', gap: '24px', fontWeight: '500' }}>
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">AI Assistant</a>
        <a href="#">Contact</a>
      </div>
      <button
  onClick={onCartClick}
  style={{
    background: '#2563eb',
    color: 'white',
    border: 'none',
    borderRadius: '10px',
    padding: '10px 18px',
    cursor: 'pointer',
    fontWeight: '600',
  }}
>
  Cart ({cartCount})
</button>
    </nav>
  );
}