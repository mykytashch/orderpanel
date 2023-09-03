# OrderPanel Setup Instructions

This document provides step-by-step instructions to set up and integrate your website with the OrderPanel system, allowing you to send orders and manage them centrally. Follow these instructions to get started.

## Prerequisites

- Basic understanding of web development concepts.
- Access to your website's codebase.
- A code editor for making changes to your website's code.

## Integration Steps

### 1. Sending Orders to OrderPanel API

To send orders to the OrderPanel API, follow these steps:

1. Make an HTTP POST request to the following endpoint: `http://your-domain.com/api/orders`
2. Include the required order information as JSON data in the request body. The order information should include `name`, `email`, `phone`, `site`, and `order_details` fields.
3. The API will respond with the newly created order ID.

### 2. Retrieving Order Information

To retrieve order information from the OrderPanel API, follow these steps:

1. Make an HTTP GET request to one of the following endpoints:
   - Get all orders: `http://your-domain.com/api/orders`
   - Get order by ID: `http://your-domain.com/api/orders/{id}`
2. The API will respond with the requested order information.

### 3. Updating Order Status

To update the status of an order through the OrderPanel API, follow these steps:

1. Make an HTTP PUT request to the following endpoint: `http://your-domain.com/api/orders/{id}/status`
2. Include the `status` parameter with the new status value in the request body.
3. The API will respond with a success message if the status is updated successfully.

### 4. Updating Order Comments

To update comments for an order through the OrderPanel API, follow these steps:

1. Make an HTTP PUT request to the following endpoint: `http://your-domain.com/api/orders/{id}/comments`
2. Include the `comments` parameter with the new comments in the request body.
3. The API will respond with a success message if the comments are updated successfully.

## Conclusion

By following these integration steps, you can seamlessly connect your website to the OrderPanel system, enabling the centralized management of orders. If you have any questions or require assistance, refer to the project's documentation or contact the development team.
