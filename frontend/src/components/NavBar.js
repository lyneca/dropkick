import React from 'react'
import { createMuiTheme, MuiThemeProvider } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid'
import logo from '../dropkick_logo.svg'; 
import Button from '@material-ui/core/Button';
// import deepOrange from '@material-ui/core/colors/deepOrange';
// import white from '@material-ui/core/colors/white';
const NavBar = () => {
    
    var orange = '#FF5722';
    var light_orange = '#FF8A65';
    var teal = '#a7ffeb';
    var black = '#212121';
    var white = '#FAFAFA'; 

    const inputProps = {
        step: 300,
        color: "#000000",
      };

    const styles = theme => ({
        button: {
            margin: theme.spacing.unit,
        },
        input: {
            display: 'none',
        },
    });

    function myFunction(e){
        console.log("hello");
        window.location.href = './unit.html';
    }

    return(
        <AppBar position="static">
                <Toolbar style={{background: black}}>
                    {/* <Grid container justify = "left" > */}
                        <img src={logo} className="App-logo" alt="logo" style={{marginLeft:50}} />
                    {/* </Grid> */}
                   
                    <Typography variant="headline" color="inherit" style={{color: light_orange,marginLeft:50}}>
                        Enter a Course 
                    </Typography>
                    
                    <TextField id="time" type="string" inputProps={inputProps} margin="dense" style={{background: white,marginLeft:20}}/>
                     {/* onClick={(e) => {myFunction()}} */}
                    <div><Button variant="contained" style={{background: white,marginLeft:10}} ><a href="./unit.html">Submit</a></Button></div>
                    
                </Toolbar>
            
        </AppBar>
    )
}
export default NavBar;