import React, { Component } from 'react'
import NavBar from './components/NavBar'
class App extends Component {
  render() {
    return (
      <div>
        <NavBar />
        <img src={require('./wallpaper-that-moves-HD9-1.jpg')} />
      </div>
    )
  }
}
export default App