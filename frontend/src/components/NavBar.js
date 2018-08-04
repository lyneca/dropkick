import React from 'react'
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid'
const NavBar = () => {
    const inputProps = {
        step: 300,
      };
    return(
        <div>
        <AppBar position="static">
            <Grid container justify = "center">
                <Toolbar>
                    <Typography variant="title" color="inherit" align = "center" >
                    Enter a Course :
                    </Typography>
                    <TextField id="time" type="string" inputProps={inputProps} />
                </Toolbar>
            </Grid>
        </AppBar>
        </div>
    )
}
export default NavBar;