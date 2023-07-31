import InventoryItem from "./InventoryItem";

export default function HomePage(props) {
    console.log(props)
    
    return (
        <>
            {props.inventory.map((iventoryitem, index) => (
                <InventoryItem 
                    key = {index}
                    title = {iventoryitem.title}
                    imgUrl = {iventoryitem.imgUrl}
                    copiesAvailable = {iventoryitem.copiesAvailable}
                    totalAvailable = {iventoryitem.totalAvailable}
                />
           ))}
        </>
    );
}