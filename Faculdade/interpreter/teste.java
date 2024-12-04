// Interface Expression (Expressão Abstrata)
interface Expression {
    int interpret();
}

// Classe TerminalExpression (Número)
class Number implements Expression {
    private int value;

    public Number(int value) {
        this.value = value;
    }

    @Override
    public int interpret() {
        return value;
    }
}

// Classe NonTerminalExpression (Soma)
class Addition implements Expression {
    private Expression leftExpression;
    private Expression rightExpression;

    public Addition(Expression leftExpression, Expression rightExpression) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }

    @Override
    public int interpret() {
        return leftExpression.interpret() + rightExpression.interpret();
    }
}

// Classe NonTerminalExpression (Subtração)
class Subtraction implements Expression {
    private Expression leftExpression;
    private Expression rightExpression;

    public Subtraction(Expression leftExpression, Expression rightExpression) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }

    @Override
    public int interpret() {
        return leftExpression.interpret() - rightExpression.interpret();
    }
}

// Classe Principal (Cliente)
public class InterpreterExample {
    public static void main(String[] args) {
        // Criando a expressão: (10 + 5) - 3
        Expression expression = new Subtraction(
            new Addition(new Number(10), new Number(5)),
            new Number(3)
        );

        // Interpretar e exibir o resultado
        int result = expression.interpret();
        System.out.println("Resultado da expressão: " + result); // Saída: 12
    }
}
