import React, {useEffect, useState} from "react";
import {Box, CircularProgress, Container, FormControl, InputLabel, MenuItem, Select} from "@mui/material";


function searchValue() {

    const [selectedValue, setSelectedValue] = useState("");
    const [procData, setProcData] = useState(null);

    useEffect(() => {
        fetch('http://localhost:20001/api/searchValue')
        .then ((response)=>response.json())
        .then((procData)=>setProcData(procData));
    }, [selectedValue])

    return (
        <>
            <h1>Price</h1>

            <Container maxWidth="100%"
                       sx={{backgroundColor: 'background.default', padding: "2rem", borderRadius: "1rem"}}>
                <Box>
                    <h2 style={{color: "white"}}>Options</h2>
                    <FormControl fullWidth>
                        <InputLabel id="Value-select-label">Value</InputLabel>
                        <Select
                            labelId="Value-select-label"
                            id="demo-simple-select"
                            value={selectedValue}
                            label="Value"
                            onChange={(e, v) => {
                                setSelectedValue(e.target.value)
                            }}
                        >
                            <MenuItem value={""}><em>None</em></MenuItem>
                            {
                                FLIGHTS.map(c => <MenuItem key={c} value={c}>{c}</MenuItem>)
                            }
                        </Select>
                    </FormControl>
                </Box>
            </Container>

            <Container maxWidth="100%" sx={{
                backgroundColor: 'info.dark',
                padding: "2rem",
                marginTop: "2rem",
                borderRadius: "1rem",
                color: "white"
            }}>
                <h2>Results <small>(PROC)</small></h2>
                {
                    procData ?
                        <ul>
                            {
                                procData.map(data => <li>{data.val}</li>)
                            }
                        </ul> :
                        selectedValue? <CircularProgress/> : "--"
                }
               
            </Container>
        </>
    );
}

export default searchValue;
