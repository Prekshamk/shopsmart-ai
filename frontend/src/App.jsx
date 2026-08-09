import Navbar from './components/Navbar';
import Hero from './components/Hero';
import FeatureCard from './components/FeatureCard';
import Footer from './components/Footer';
import ProductCard from './components/ProductCard';
import AIAssistant from './components/AIAssistant';

function App() {
  return (
    <div style={{ fontFamily: 'Arial', backgroundColor: '#f8fafc', minHeight: '100vh' }}>
      <Navbar />
      <Hero />

      <section
        style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '24px',
          padding: '40px 20px',
          flexWrap: 'wrap',
        }}
      >
        <FeatureCard
          title="AI Recommendations"
          description="Get products tailored to your preferences and budget."
        />

        <FeatureCard
          title="Smart Price Comparison"
          description="Compare prices across stores instantly before purchasing."
        />

        <FeatureCard
          title="Eco-Friendly Choices"
          description="Discover sustainable products with lower environmental impact."
        />
      </section>

      <section style={{ padding: '60px 20px' }}>
  <h2
    style={{
      textAlign: 'center',
      fontSize: '36px',
      marginBottom: '40px',
      color: '#111827',
    }}
  >
    Featured Products
  </h2>

  <div
    style={{
      display: 'flex',
      justifyContent: 'center',
      gap: '24px',
      flexWrap: 'wrap',
    }}
  >
    <ProductCard
      name="Wireless Headphones"
      price="2,499"
      image="https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?w=500"
    />

    <ProductCard
      name="Smart Watch"
      price="3,999"
      image="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"
    />

    <ProductCard
      name="Eco Water Bottle"
      price="799"
      image="https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500"
    />
  </div>
</section>

<AIAssistant />

      <Footer />
    </div>
  );
}

export default App;