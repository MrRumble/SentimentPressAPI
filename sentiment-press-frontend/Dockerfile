# Use the official Node.js image as the base
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first (improves caching)
COPY package.json package-lock.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the frontend app
RUN npm run build

# Expose the port the frontend runs on
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
