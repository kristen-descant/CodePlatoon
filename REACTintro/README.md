# Video Store

## Usage

Install dependencies

```sh
npm install
```

Run dev server

```sh
npm run dev
```

## Assignment

### Goal

Use the data provided in `src/data/inventory.json` to create a Video Store App

> You can import a json file like so:
>
> ```js
> import inventory from "./data/inventory.json";
> ```
>
> `inventory` will now hold the json object

### Sub Goals

1. Create a `components` folder within the `src` folder for your own components.

2. Create a `HomePage` component in the `components` folder and reference it within the `App` component

3. Pass the `inventory` json object from `App` to `HomePage` using props

4. The `HomePage` should showcase the entire inventory by mapping the `inventory` object using `.map`

5. For each inventory item, render a unique `InventoryItem` component and pass the relevant data (for that specific inventory item) as props

6. Create an `InventoryItem` component that uses the props passed in to render the item with:

   - title
   - image
   - copies available / total copies
   - a 'checkout' button

7. Make the checkout button trigger an `alert()` that reports how many copies are currently available. Tomorrow we will learn how to actually update this amount with useState.

Bonus:

8. disable the checkout button if there are no available copies to check out

9. Use css to create a nice UI (flexbox)

### Example Solution

A solution is provided for you in the `solution` branch, but try to use it only if you are stuck.

Switch the the branch with:

```sh
git checkout solution
```

> You may need to first commit any un-commited work on `main`

Just like in main, install and run dev to see the desired output:

```sh
npm install
npm run dev
```
