
This Django app serves as a comprehensive order and invoice management system for a garment store. It facilitates smooth operations by automating order handling, tailor task assignments, payment tracking, and report generation.

---

 Features and Workflow

 1. Order Management:
   - Order Storage: 
     - When a new order is received, it is stored in the system with details such as customer name, contact, garment specifications, due date, and payment status.
   - Order Assignment:
     - Each order is assigned to a tailor from the tailor database. Tailors are selected based on predefined criteria, such as availability or expertise.

 2. Invoice Generation:
   - Order Invoice:
     - Upon receiving payment, the system generates an invoice for the customer. This invoice includes:
       - Order ID
       - Customer details
       - Order details (garment type, specifications, etc.)
       - Payment details
   - Daily Billing Report:
     - The system can generate a summary of orders for a specific day, such as:
       - Orders Received: A list of all orders placed on a particular day.
       - Orders Completed: A summary of orders completed and ready for delivery.

 3. Task Assignment for Tailors:
   - Tailor Slip Generation:
     - A task slip is generated for tailors, providing them with details about their assigned orders. 
     - This slip includes:
       - Tailor's name
       - Assigned order details
       - Deadlines
   - This ensures that tailors have a clear understanding of their tasks and deadlines.

 4. Order Tracking and Status Update:
   - Payment Status:
     - The system updates the status of an order when the payment is received.
     - Payment tracking ensures seamless financial management.
   - Order Status:
     - Tracks orders through various stages (e.g., Received, In Progress, Completed).

 5. Reports and Summaries:
   - The system can generate detailed reports for:
     - Orders received on a specific day.
     - Orders completed on a specific day.
   - These reports aid in managing workflow and monitoring store performance.

This system streamlines garment store operations, reducing manual work, improving accuracy, and enhancing productivity. 

Order Page

![image](https://github.com/user-attachments/assets/02a85f80-2584-4c62-a8dd-f69effb2ad61)


Daily Sales Page

![image](https://github.com/user-attachments/assets/a3f76b2e-c25a-40f0-95a2-30acd1ab762f)

Sales categorised as per Tailor

![image](https://github.com/user-attachments/assets/03170aea-e37f-44dc-a3e1-2b6141114cbd)

Generated PDFs

![image](https://github.com/user-attachments/assets/bbf24c2c-9ad9-4c0d-8aaa-a0cf3c504474)

![image](https://github.com/user-attachments/assets/f8a69277-a21a-4043-94fa-41f2cb70d6db)

![image](https://github.com/user-attachments/assets/6d7b6178-7e14-4852-99ba-8651f12fe936)

![image](https://github.com/user-attachments/assets/3d6ce8b3-790e-46f2-ba2d-d3f114003e9b)


