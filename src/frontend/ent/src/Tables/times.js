import {useEffect, useState} from "react";
import {
    CircularProgress,
    Pagination,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow
} from "@mui/material";



function Times() {

    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [data, setData] = useState([]);
    const [maxDataSize] = useState(data.length);

    useEffect(() => {
        fetch('http://localhost:20001/api/times')
        .then ((response)=>response.json())
        .then((data)=>setData(data));
       
    }, [page])

    return (
        <>
            <h1>Times </h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" width={"1px"} align="center">ID</TableCell>
                            <TableCell>Departure</TableCell>
                            <TableCell> Arrival</TableCell>
                            <TableCell>Created on</TableCell>
                            <TableCell>Updated on</TableCell>

                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            data ?
                                data.map((row) => (
                                    <TableRow
                                        key={row.id}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.id}</TableCell>
                                        <TableCell component="td" scope="row">
                                            {row.departure}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.arrival}
                                        </TableCell>
                                        
                                        <TableCell component="td" align="center" scope="row">
                                            {row.created_on}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.updated_on}
                                        </TableCell>
                                        
                                
                                    </TableRow>
                                ))
                                :
                                <TableRow>
                                    <TableCell colSpan={5}>
                                        <CircularProgress/>
                                    </TableCell>
                                </TableRow>
                        }
                    </TableBody>
                </Table>
            </TableContainer>
            {
                maxDataSize && <div style={{background: "black", padding: "1rem"}}>
                    <Pagination style={{color: "black"}}
                                variant="outlined" shape="rounded"
                                color={"primary"}
                                onChange={(e, v) => {
                                    setPage(v)
                                }}
                                page={page}
                                count={Math.ceil(maxDataSize / PAGE_SIZE)}
                    />
                </div>
            }


        </>
    );
}

export default Times;