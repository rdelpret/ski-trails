import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { ThemeProvider, createTheme } from '@mui/material/styles';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});


ReactDOM.render(
  <React.StrictMode>
     <ThemeProvider theme={darkTheme}>
        <App />
      </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
