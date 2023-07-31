export default function InventoryItem(props) {
    const {title, imgUrl, copiesAvailable, totalAvailable}= props;

    return (
      <div className="inventory">
        <img src={imgUrl}/>
        <h1>{title}</h1>
        <span>Copies Available: {copiesAvailable}   </span>
        <span>    Total Available: {totalAvailable}</span>
        <br />
        <button disabled = {copiesAvailable === 0}>Check Out</button>
      </div>
    );
  }