# OrderPanel API Documentation

## Introduction

OrderPanel provides API endpoints to allow websites to send orders and retrieve order information for centralized management. This documentation outlines the available API endpoints, their functionalities, and the required parameters.

## Base URL

The base URL for the OrderPanel API is: `http://your-domain.com`

## Authentication

No authentication is required for sending orders through the API. However, for retrieving orders and other sensitive operations, an authentication mechanism should be implemented.

## API Endpoints

### 1. Create an Order

Endpoint: `POST /api/orders`

#### Request Parameters

| Parameter     | Type     | Description                           |
|---------------|----------|---------------------------------------|
| name          | string   | Customer's name                       |
| email         | string   | Customer's email                      |
| phone         | string   | Customer's phone number               |
| site          | string   | Website identifier                    |
| order_details | JSON     | JSON data containing order details    |

#### Response

The API will respond with the newly created order ID.

---

### 2. Get All Orders

Endpoint: `GET /api/orders`

#### Response

The API will respond with a list of all orders available in the system.

---

### 3. Get Order by ID

Endpoint: `GET /api/orders/{id}`

#### Request Parameter

| Parameter | Type   | Description         |
|-----------|--------|---------------------|
| id        | int    | Order ID to retrieve|

#### Response

The API will respond with the order details associated with the provided ID.

---

### 4. Update Order Status

Endpoint: `PUT /api/orders/{id}/status`

#### Request Parameters

| Parameter | Type    | Description                 |
|-----------|---------|-----------------------------|
| id        | int     | Order ID to update          |
| status    | string  | New status for the order    |

#### Response

The API will respond with a success message if the status is updated successfully.

---

### 5. Update Order Comments

Endpoint: `PUT /api/orders/{id}/comments`

#### Request Parameters

| Parameter | Type    | Description                   |
|-----------|---------|-------------------------------|
| id        | int     | Order ID to update            |
| comments  | string  | New comments for the order    |

#### Response

The API will respond with a success message if the comments are updated successfully.

---

## Conclusion

The OrderPanel API allows websites to seamlessly send and retrieve order information for centralized management. By integrating these endpoints into your website, you can efficiently manage orders through the OrderPanel dashboard.

For any inquiries or assistance, please refer to the project's documentation or contact the development team.
