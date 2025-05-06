import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ConcatServer extends UnicastRemoteObject implements ConcatService {

    protected ConcatServer() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }

    public static void main(String[] args) {
        try {
            ConcatServer server = new ConcatServer();
            Naming.rebind("rmi://localhost/ConcatService", server);
            System.out.println("Server is running...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
