import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const trailsTable = ({ trails }) => {
return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="right">Resort</TableCell>
            <TableCell align="right">Area</TableCell>
            <TableCell align="right">Trail</TableCell>
            <TableCell align="right">Difficulty</TableCell>
            <TableCell align="right">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
           { (trails.length > 0) ? trails.map( (trail, index) => {
           return (
            <TableRow
              key={index}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{ trail[0] }</TableCell>
              <TableCell align="right">{ trail[1] }</TableCell>
              <TableCell align="right">{ trail[2] }</TableCell>
              <TableCell align="right">{ trail[3] }</TableCell>
              <TableCell align="right">{ trail[4] }</TableCell>
            </TableRow>
          )
         }) : <TableRow><TableCell colSpan="5" align="center">Loading...</TableCell></TableRow> }
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default trailsTable