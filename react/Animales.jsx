import { useEffect, useState } from "react";
export default function Animales() {
  const [animales, setAnimales] = useState([]);
  const [error, setError] = useState("");
  useEffect(() => {
    fetch("http://127.0.0.1:8001/api/animales/")
      .then(r => { if (!r.ok) throw Error("Error al cargar"); return r.json(); })
      .then(setAnimales).catch(e => setError(e.message));
  }, []);
  return <><p>{error}</p><ul>{animales.map(a =>
    <li key={a.id}>{a.nombre} - {a.especie} - {a.raza} - {a.edad} años</li>
  )}</ul></>;
}
