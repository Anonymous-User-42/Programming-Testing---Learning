import NumButton from "./components/NumButton";

function App() {
  return (
    <>
      <div className="bg-white text-center">
        <NumButton tag={["AC", "+/-", "%"]} />
        <NumButton tag={[7, 8, 9]} />
        <NumButton tag={[4, 5, 6]} />
        <NumButton tag={[1, 2, 3]} />
      </div>
    </>
  );
}

export default App;
