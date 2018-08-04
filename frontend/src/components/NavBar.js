import React from 'react'
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid'
const NavBar = () => {
    
    var orange = '#ff9800';
    var teal = '#a7ffeb';
    var black = '#212121';
    var white = '#FAFAFA'; 

    const inputProps = {
        step: 300,
      };
    
    return(
        <div>
        <AppBar position="static">
            <Grid container justify = "center" style={{background: black}}>
                <Toolbar>
                    <Typography variant="headline" color="inherit" style={{color: orange}}>
                        Enter a Course 
                    </Typography>
                    <TextField id="time" type="string" inputProps={inputProps} margin="dense" fullWidth={true} style={{background: white}}/>
                </Toolbar>
            </Grid>
        </AppBar>
        </div>
    )
}
export default NavBar;