function NumButton({ tag }) {
  return (
    <div>
      <button
        onClick={console.log(tag[0])}
        className="text-white bg-black-50 rounded-full"
      >
        {tag[0]}
      </button>
      <button
        onClick={console.log(tag[1])}
        className="text-white bg-black-50 rounded-full"
      >
        {tag[1]}
      </button>
      <button
        onClick={console.log(tag[2])}
        className="text-white bg-black-50 rounded-full"
      >
        {tag[2]}
      </button>
    </div>
  );
}

export default NumButton;
