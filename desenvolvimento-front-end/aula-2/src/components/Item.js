import { useState } from "react";

export default function Item(props) {
    // console.log(props)

    const [quantity, setQuantity] = useState(1)
    const [valueButton, setValueButton] = useState(true)
    const product = props.product

    // Função para subtrair o valor da quantidade de um produto
    const minus = () => {
        (quantity - 1) === 1 ? setValueButton(true) : setValueButton(false)
        if (quantity !== 1) {
            setQuantity(quantity - 1)
        }
    }


    // Função para somar valor da quantidade de um produto
    const plus = () => {
        setValueButton(false)
        setQuantity(quantity + 1)
    }

    // Função para comprar um produto informando o preço final
    const buyProduct = () => {
        if (window.confirm(`Preço final: ${Math.round((product.price * quantity) * 100) / 100}`)) {
            alert('Produto comprado com sucesso!')
            setQuantity(1)
        }
    }


    return (
        <article className="product">
            <img src={product.image} alt="product"/>
            <h3 className="price-product">
                R$ <span>{product.price}</span>
            </h3>
            <p className="name-product">{product.title}</p>
            <div className="quantity">
                <span >Quantidade:</span>
                <button disabled={valueButton} className="minus" onClick={minus}>-</button>
                <span>{quantity}</span>
                <button className="plus" onClick={plus}>+</button>
            </div>
            <button className="buy" onClick={buyProduct}>Comprar</button>
        </article>

    );
}