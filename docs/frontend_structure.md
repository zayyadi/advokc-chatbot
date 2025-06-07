# Frontend Chatbot Structure (React/Next.js)

This document outlines the proposed structure for the ADVOKC Chatbot frontend, likely to be built using React.js or Next.js.

## 1. Core Technologies

-   **Framework/Library:** React.js (potentially with Next.js for server-side rendering, routing, and API routes if beneficial).
-   **State Management:** React Context API for simpler global state (e.g., user session, theme). For more complex state, consider Zustand or Redux Toolkit.
-   **Styling:** CSS Modules, Tailwind CSS, or a component library like Material-UI/Chakra UI.
-   **HTTP Client:** `fetch` API or a library like `axios` for communicating with the backend.

## 2. Project Directory Structure (Conceptual)

```
frontend/
├── public/ # Static assets
│   ├── index.html
│   └── ...
├── src/
│   ├── components/ # Reusable UI components
│   │   ├── ChatWindow/
│   │   │   ├── ChatWindow.js
│   │   │   ├── MessageList.js
│   │   │   ├── MessageItem.js
│   │   │   └── ChatWindow.module.css
│   │   ├── MessageInput/
│   │   │   ├── MessageInput.js
│   │   │   └── MessageInput.module.css
│   │   ├── PromiseDisplay/
│   │   │   ├── PromiseCard.js
│   │   │   ├── PromiseList.js
│   │   │   └── PromiseFilter.js
│   │   ├── common/ # Buttons, Modals, Loaders etc.
│   │   │   ├── Button.js
│   │   │   └── LoadingSpinner.js
│   ├── pages/ # Top-level page components (especially if using Next.js or React Router)
│   │   ├── HomePage.js
│   │   ├── ChatPage.js
│   │   ├── PromisesPage.js
│   │   ├── AdvokcInfoPage.js
│   │   └── AboutPage.js
│   ├── services/ # API interaction layer
│   │   ├── apiClient.js # Configured Axios instance or fetch wrappers
│   │   ├── chatService.js
│   │   ├── promiseService.js
│   │   └── advokcInfoService.js
│   ├── contexts/ # React Context API for state management
│   │   ├── AuthContext.js
│   │   └── ThemeContext.js
│   ├── hooks/ # Custom React hooks
│   │   └── useChat.js
│   ├── layouts/ # Layout components (e.g., MainLayout with Navbar and Footer)
│   │   └── MainLayout.js
│   ├── App.js       # Main application component
│   ├── index.js     # Entry point of the React application
│   └── setupTests.js # Jest/React Testing Library setup
├── .env             # Environment variables
├── package.json
└── README.md
```

## 3. Key Components

### 3.1. `ChatWindow`
    -   **`ChatWindow.js`**: Main container for the chat interface.
        -   Manages the conversation flow.
        -   Fetches responses from the backend via `chatService`.
    -   **`MessageList.js`**: Displays the list of messages (user queries and bot responses).
        -   Scrolls automatically to the latest message.
    -   **`MessageItem.js`**: Renders an individual message bubble (differentiating user vs. bot).
        -   May include timestamps, sender avatars (optional).
        -   Could display sources or citations if provided by the RAG backend.

### 3.2. `MessageInput`
    -   **`MessageInput.js`**: Text input field for users to type their queries.
        -   Handles message submission (on Enter key or send button click).
        -   May include a send button, microphone icon for voice input (future).
        -   Could have loading indicators while waiting for a response.

### 3.3. `PromiseTrackerDisplay` (or components within `PromisesPage.js`)
    -   **`PromiseList.js`**: Displays a list of promises fetched from the backend.
    -   **`PromiseCard.js`**: Renders an individual promise with its details (title, description, status, politician, date made, source).
        -   May include options to view more details or evidence.
    -   **`PromiseFilter.js`**: Allows users to filter promises (e.g., by status, politician, category).
    -   (Optional) **`PromiseCreateForm.js`**: A form for administrators to add new promises (if frontend submission is required).

### 3.4. `AdvokcInfoPage`
    -   Displays static and dynamic information about ADVOKC.
    -   Could fetch data from `/advokc_info` backend endpoint.
    -   Components for different sections (e.g., Mission, Contact, Campaigns).

### 3.5. Layout and Navigation
    -   **`MainLayout.js`**: Common structure including a navigation bar (Navbar) and footer.
    -   **`Navbar.js`**: Links to different pages (Chat, Promises, ADVOKC Info, About).

## 4. State Management

-   **Local Component State (`useState`, `useReducer`):** For component-specific data (e.g., input field values, loading states within a component).
-   **React Context API:** For global state that doesn't change too frequently or is needed by many components across different levels of the tree.
    -   `SessionContext`: Could manage a user session ID for the chat.
    -   `ThemeContext`: For light/dark mode.
    -   `NotificationContext`: For displaying global notifications/alerts.
-   **Zustand/Redux Toolkit (Optional):** If state management becomes very complex with many inter-dependencies and frequent updates, these libraries offer more robust solutions with better developer tools and performance optimizations. Start with Context API and evaluate if a more powerful solution is needed.

## 5. Routing

-   If using **Next.js**, its file-system based routing will be used for pages.
-   If using plain **React (e.g., Create React App)**, `react-router-dom` will be used for client-side routing.

## 6. API Interaction (`services/`)

-   Create dedicated service modules (`chatService.js`, `promiseService.js`) to encapsulate API call logic.
-   Use a centralized API client (e.g., an `axios` instance with base URL and default headers) in `apiClient.js`. This makes it easier to manage API configurations (e.g., authentication tokens if added later).

## 7. Styling

-   **Tailwind CSS:** For utility-first CSS, allowing for rapid UI development.
-   **CSS Modules:** For component-scoped CSS, preventing style conflicts.
-   A combination of both can be effective.
-   Consider a UI component library like **Material-UI**, **Chakra UI**, or **Ant Design** if a pre-built set of themed components is desired, which can speed up development.

This structure provides a flexible foundation for the frontend. Specific implementation details will be refined during development.
