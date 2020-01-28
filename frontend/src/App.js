import React from 'react';
import Bookshop from './components/Bookshop';
import Header from './components/layout/Header';
import Body from './components/layout/Body';
import './App.css';
import axios from 'axios';


class App extends React.Component {
  state = {
    books: [],
    cart: []
  }
  
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/books/?format=json')
      .then(res => this.setState({ books: res.data}))
  }



  render() {
  return (
    <div className="App">
      <Header />
      <Body />
      <Bookshop books={this.state.books}/>
    </div>
  );
  }
}

export default App;