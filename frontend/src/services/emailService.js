import axios from "axios";

export const sendEmail = async (emailData) => {
    try{
        const endpoint = 'http://127.0.0.1:8000/api/send-email/';
        const response = await axios.post(endpoint, emailData);
        //console.log(endpoint.data); //console to see if it captures email
        return response;
    } catch{
        console.error("Unable to sent email:", error); //display error caught
        throw error;
    }
}