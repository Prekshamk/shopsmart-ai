function App() {
  return (
    <div style={{ fontFamily: 'Arial', backgroundColor: '#f8fafc', minHeight: '100vh' }}>

      {/* Navbar */}
      <nav style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '20px 60px',
        backgroundColor: 'white',
        boxShadow: '0 2px 8px rgba(0,0,0,0.05)'
      }}>
        <h2 style={{ color: '#1e3a8a' }}>ShopSmart AI</h2>
        <div style={{ display: 'flex', gap: '20px' }}>
          <a href="#" style={{ textDecoration: 'none', color: '#374151' }}>Home</a>
          <a href="#" style={{ textDecoration: 'none', color: '#374151' }}>Products</a>
          <a href="#" style={{ textDecoration: 'none', color: '#374151' }}>AI Assistant</a>
          <a href="#" style={{ textDecoration: 'none', color: '#374151' }}>Contact</a>
        </div>
      </nav>

      {/* Hero Section */}
      <section style={{
        textAlign: 'center',
        padding: '100px 20px'
      }}>
        <h1 style={{
          fontSize: '56px',
          color: '#111827',
          marginBottom: '20px'
        }}>
          Shop Smarter with AI
        </h1>

        <p style={{
          fontSize: '22px',
          color: '#4b5563',
          maxWidth: '800px',
          margin: '0 auto 30px'
        }}>
          Personalized product recommendations, smart price comparison,
          and sustainable shopping choices powered by artificial intelligence.
        </p>

        <div style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '15px',
          flexWrap: 'wrap'
        }}>
          <button style={{
            padding: '15px 30px',
            fontSize: '18px',
            backgroundColor: '#2563eb',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer'
          }}>
            Start Shopping
          </button>

          <button style={{
            padding: '15px 30px',
            fontSize: '18px',
            backgroundColor: 'white',
            color: '#2563eb',
            border: '2px solid #2563eb',
            borderRadius: '12px',
            cursor: 'pointer'
          }}>
            Ask AI Assistant
          </button>
        </div>
      </section>

      {/* Features */}
      <section style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '20px',
        padding: '40px 60px 80px'
      }}>

        <div style={{
          backgroundColor: 'white',
          padding: '30px',
          borderRadius: '16px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.05)'
        }}>
          <h3 style={{ color: '#111827' }}>AI Recommendations</h3>
          <p style={{ color: '#4b5563' }}>
            Get products tailored to your preferences and budget.
          </p>
        </div>

        <div style={{
          backgroundColor: 'white',
          padding: '30px',
          borderRadius: '16px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.05)'
        }}>
          <h3 style={{ color: '#111827' }}>Smart Price Comparison</h3>
          <p style={{ color: '#4b5563' }}>
            Compare prices across stores instantly before purchasing.
          </p>
        </div>

        <div style={{
          backgroundColor: 'white',
          padding: '30px',
          borderRadius: '16px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.05)'
        }}>
          <h3 style={{ color: '#111827' }}>Eco-Friendly Choices</h3>
          <p style={{ color: '#4b5563' }}>
            Discover sustainable products with lower environmental impact.
          </p>
        </div>

      </section>

      {/* Footer */}
      <footer style={{
        textAlign: 'center',
        padding: '30px',
        color: '#6b7280',
        borderTop: '1px solid #e5e7eb'
      }}>
        © 2026 ShopSmart AI by Preksha • Built with React + Vite
      </footer>

    </div>
  );
}

export default App;