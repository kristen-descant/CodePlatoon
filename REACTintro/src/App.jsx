import inventory from "./data/inventory.json";
import HomePage from "./components/HomePage";

export default function App() {
  console.log(inventory);

  return (
    <div id="app">
      <header>
        <h1>Video Store</h1>
      </header>
      <main>
        <h1>Home Page goes here</h1>
        <div className="homepage">
          <HomePage inventory={inventory}/>
        </div>
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}
