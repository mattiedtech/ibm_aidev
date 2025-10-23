process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;
const express = require('express');
const path = require('path');
const { OpenAIApi } = require('./openai');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public'));
});

app.post('/getChatbotResponse', async (req, res) => {
    const userMessage = req.body.userMessage;

    // Use OpenAI API to get chatbot response
    const chatbotResponse = await OpenAIApi.getChatbotResponse(userMessage);

    // Send chatbot response back to client
    res.json({ chatbotResponse });
});
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});