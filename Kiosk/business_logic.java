import java.io.*;
import com.google.gson.Gson;

class DataManager {
    private String productsFile;
    private String transactionsFile;
    private Gson gson;
    private Product[] products;
    private Transaction[] transactions;

    public DataManager(String productsFile, String transactionsFile) {
        this.productsFile = productsFile;
        this.transactionsFile = transactionsFile;
        this.gson = new Gson();
        loadProducts();
        loadTransactions();
    }

    private void loadProducts() {
        try (Reader reader = new FileReader(productsFile)) {
            products = gson.fromJson(reader, Product[].class);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void loadTransactions() {
        try (Reader reader = new FileReader(transactionsFile)) {
            transactions = gson.fromJson(reader, Transaction[].class);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void saveData() {
        try (Writer writer = new FileWriter(productsFile)) {
            gson.toJson(products, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Implement other data management functions as needed
}

class Product {
    private String name;
    private double buyingPrice;
    private double sellingPrice;
    private int quantity;

    // Constructor, getters, and setters...
}

class Transaction {
    private String itemName;
    private int quantity;
    private double price;
    private String type; // sale or expense
    private String timestamp;

    // Constructor, getters, and setters...
}

public class Main {
    public static void main(String[] args) {
        String productsFile = "products.json";
        String transactionsFile = "transactions.json";
        DataManager dataManager = new DataManager(productsFile, transactionsFile);

        // Use dataManager to perform data management operations
    }
}
