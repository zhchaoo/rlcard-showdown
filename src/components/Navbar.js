import React, { useEffect, useState } from "react";
import { Link, useLocation } from 'react-router-dom';
import logo_white from "../assets/images/logo_white.png";
import GitHubIcon from "@material-ui/icons/GitHub";
import AppBar from "@material-ui/core/AppBar";
import axios from 'axios';

function Navbar({subtitleMap}) {
    const [stars, setStars] = useState('...');
    let location = useLocation();
    console.log(location.pathname, subtitleMap);
    const subtitle = subtitleMap[location.pathname];

    useEffect(() => {
        axios.get("https://api.github.com/repos/datamllab/rlcard")
            .then(res=>{
                setStars(res.data.stargazers_count);
            });
    }, [])

    return (
        <AppBar position="fixed" className={"header-bar-wrapper"}>
        </AppBar>
        )

}

export default Navbar;
