
class FalhaAutenticacaoException(Exception):
    """Sinaliza inconsistência no usuário ou na senha fornecidos."""
    pass

class AcessoBloqueadoException(Exception):
    """Sinaliza o esgotamento do limite de tentativas de login permitidas."""
    pass


class ControladoraAcesso:
    def __init__(self, login_esperado="admin", senha_esperada="admin123", limite_falhas=3):
        """
        Define as credenciais padrão de acesso e o limite de tentativas.
        """
        self._login_esperado = login_esperado
        self._senha_esperada = senha_esperada
        self.limite_falhas = limite_falhas
        self.contador_falhas = 0

    def validar_credenciais(self, login, senha):
        """
        Valida o par de usuário e senha recebidos.

        Dispara:
        - AcessoBloqueadoException: Caso o limite de erros já tenha sido atingido.
        - FalhaAutenticacaoException: Quando o login ou a senha estão incorretos.
        """
        
        if self.contador_falhas >= self.limite_falhas:
            raise AcessoBloqueadoException("Acesso temporariamente suspenso por medidas de segurança.")

        
        if login != self._login_esperado or senha != self._senha_esperada:
            self.contador_falhas += 1
            chances_restantes = self.limite_falhas - self.contador_falhas
            
            if self.contador_falhas >= self.limite_falhas:
                raise AcessoBloqueadoException("Sistema bloqueado! Quantidade máxima de falhas atingida.")
            
            raise FalhaAutenticacaoException(
                f"Dados de acesso incorretos. Você ainda tem {chances_restantes} tentativa(s)."
            )

        
        self.contador_falhas = 0
        return True


def iniciar_painel_login():
    """
    Gerencia a interação com o usuário via terminal.
    """
    gerenciador = ControladoraAcesso(login_esperado="dev_user", senha_esperada="pass123", limite_falhas=3)
    
    print("------------------------------------------")
    print("      PORTAL DE AUTENTICAÇÃO - SISTEMA    ")
    print("------------------------------------------")
    
    while True:
        try:
            usuario_input = input("\n[ENTRADA] Informe o Usuário: ")
            senha_input = input("[ENTRADA] Informe a Senha:   ")
            
            
            if gerenciador.validar_credenciais(usuario_input, senha_input):
                print("\n[SUCESSO] Login realizado! Redirecionando para a área logada...")
                break
                
        except FalhaAutenticacaoException as erro:
            
            print(f"[ALERTA] {erro}")
            
        except AcessoBloqueadoException as erro:
            
            print(f"\n[NEGADO] {erro}")
            print("Finalizando aplicação...")
            break


if __name__ == "__main__":
    iniciar_painel_login()