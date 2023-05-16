import { useEffect, useState } from "react"
import Item from "../components/Item"
import banner from '../assets/banner.png'
import axios from 'axios'

export default function Products() {
  const [productList, setProductList] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/produtos')
      .then(res => setProductList(res.data.produtos))
      .catch(error => console.log(error))
  }, [])

  return (
    <div className="content-product">
      <header>
        <div className="user">
          <span>Usuário</span>
        </div>
      </header>

      <section className="banner">
        <img src={banner} alt="Banner" />
      </section>

      <section className="main-products">
        {productList.map((p, index) => (
          <Item key={index} product={p} />
        ))}
      </section>
      <footer></footer>
    </div>
  )
}
