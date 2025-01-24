import { BrowserRouter, Routes, Route } from "react-router-dom";
import { PaginaIncial } from "./pages/PaginaIncial";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<div>Hola Mundo - Clase X</div>} />
        <Route path="/pagina" element={<PaginaIncial />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
