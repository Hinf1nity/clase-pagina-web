import { useForm } from "react-hook-form";
import { InputButton } from "../components/InputButton";
import { Container, Row, Col, Button } from "react-bootstrap";
import { useState } from "react";

export function PaginaIncial() {
  const { register, handleSubmit } = useForm();
  const { register: register2, handleSubmit: handleSubmit2 } = useForm();
  const [resultado, setResultado] = useState(0);
  const onSubmit = handleSubmit((data) => {
    console.log(data);
    setResultado(data.numero1 + resultado);
  });
  const onSubmit1 = handleSubmit2((data) => {
    console.log(data);
    setResultado(data.numero2 + resultado);
  });
  return (
    <div>
      <h1>PaginaIncial</h1>
      <p>Esta es la página inicial de la aplicación</p>
      <Container>
        <Row>
          <Col>
            <InputButton
              register={register}
              onSubmit={onSubmit}
              tam="sm"
              numero="numero1"
            />
          </Col>
          <Col>
            <InputButton
              register={register2}
              onSubmit={onSubmit1}
              tam="lg"
              numero="numero2"
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <h2>Resultado: {resultado}</h2>
          </Col>
          <Col>
            <Button variant="danger" onClick={() => setResultado(0)}>
              Limpiar
            </Button>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
