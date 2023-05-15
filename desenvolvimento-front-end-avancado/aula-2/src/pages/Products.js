import { useState } from "react"
import Item from "../components/Item"
import products from '../products.json'
import banner from '../assets/banner.png'

export default function Products() {
  const [productList, setProductList] = useState(products.bottles)

  return (
    <div className="content-product">
      <header>
        <div className="user">
          <span>Usuário</span>
        </div>
      </header>

      <section className="banner">
        <img src={banner} alt="Banner"/>
      </section>

      <section className="main-products">
        {productList.map((p, index) => (
          <Item key={index} product={p}/>
        ))}
      </section>
      <footer></footer>
    </div>
  )
}
