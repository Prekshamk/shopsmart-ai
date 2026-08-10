import { useState } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import FeatureCard from './components/FeatureCard';
import ProductCard from './components/ProductCard';
import AIAssistant from './components/AIAssistant';
import Footer from './components/Footer';
import './App.css';

export default function App() {
  const [cartItems, setCartItems] = useState([]);
  const [showCart, setShowCart] = useState(false);

  const addToCart = (product) => {
    setCartItems((prev) => [...prev, product]);
  };

  const products = [
    {
      name: 'Wireless Headphones',
      price: '₹2,499',
      image:
        'https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?q=80&w=600&auto=format&fit=crop',
    },
    {
      name: 'Smart Watch',
      price: '₹3,999',
      image:
        'https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=600&auto=format&fit=crop',
    },
    {
      name: 'Eco Water Bottle',
      price: '₹799',
      image:
        'https://images.unsplash.com/photo-1602143407151-7111542de6e8?q=80&w=600&auto=format&fit=crop',
    },
  ];

  const total = cartItems.reduce(
    (sum, item) =>
      sum + Number(item.price.replace('₹', '').replace(',', '')),
    0
  );

  return (
    <>
      <Navbar
        cartCount={cartItems.length}
        onCartClick={() => setShowCart(!showCart)}
      />

      <Hero />

      {showCart && (
        <div
          style={{
            maxWidth: '900px',
            margin: '20px auto',
            background: '#fff',
            padding: '24px',
            borderRadius: '16px',
            boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
          }}
        >
          <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>
            Shopping Cart
          </h2>

          {cartItems.length === 0 ? (
            <p style={{ textAlign: 'center' }}>Your cart is empty.</p>
          ) : (
            <>
              {cartItems.map((item, index) => (
                <div
                  key={index}
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    padding: '12px 0',
                    borderBottom: '1px solid #e5e7eb',
                  }}
                >
                  <span>{item.name}</span>
                  <span>{item.price}</span>
                </div>
              ))}

              <h3 style={{ textAlign: 'center', marginTop: '20px' }}>
                Total: ₹{total}
              </h3>
            </>
          )}
        </div>
      )}

      <section className="features">
        <FeatureCard
          title="AI Recommendations"
          text="Get products tailored to your preferences and budget."
        />

        <FeatureCard
          title="Smart Price Comparison"
          text="Compare prices across stores instantly before purchasing."
        />
      </section>

      <section className="products">
        <h2>Featured Products</h2>

        <div className="product-grid">
          {products.map((product) => (
            <ProductCard
              key={product.name}
              name={product.name}
              price={product.price}
              image={product.image}
              onAddToCart={() => addToCart(product)}
            />
          ))}
        </div>
      </section>

      <AIAssistant />

      <Footer />
    </>
  );
}