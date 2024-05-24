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



function Flights() {

    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [data, setData] = useState([]);
    const [maxDataSize] = useState(data.length);

    useEffect(() => {
        fetch('http://localhost:20001/api/flights')
        .then ((response)=>response.json())
        .then((data)=>setData(data));
       
    }, [page])

    return (
        <>
            <h1>Flights</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" width={"1px"} align="center">ID</TableCell>
                            <TableCell>Name</TableCell>
                            <TableCell>Id airline</TableCell>
                            <TableCell>Id routes</TableCell>
                            <TableCell>Id classes</TableCell>
                            <TableCell>Price</TableCell>
                            <TableCell>Stops</TableCell>
                            <TableCell>Created on</TableCell>
                            <TableCell>Updated on</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            data ?
                                data.map((row, index) => (
                                    <TableRow
                                        key={index}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center" scope="row">
                                            {row.id}
                                            </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.name}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.flight}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.id_airline}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.id_routes}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.id_classes}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.price}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.stops}
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
                                    <TableCell colSpan={10}>
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

export default Flights;
