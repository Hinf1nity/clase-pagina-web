import { Button, Form, InputGroup } from "react-bootstrap";
import PropTypes from "prop-types";

export function InputButton({ register, onSubmit, tam, numero }) {
  // Add 'register' to the props validation
  return (
    <form onSubmit={onSubmit}>
      <InputGroup size={tam}>
        <InputGroup.Text>Numero 1:</InputGroup.Text>
        <Form.Control
          type="number"
          {...register(numero, { valueAsNumber: true })}
        />
      </InputGroup>
      <Button type="submit">Enviar</Button>
    </form>
  );
}

InputButton.propTypes = {
  register: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired,
  tam: PropTypes.string.isRequired,
  numero: PropTypes.string.isRequired,
};
