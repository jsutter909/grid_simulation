import React, { useState } from "react";
import ChartistGraph from "react-chartist";
// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";
import TextField from "@mui/material/TextField";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import FilledInput from "@mui/material/FilledInput";
import InputAdornment from "@mui/material/InputAdornment";
import { TimePicker } from "@mui/x-date-pickers/TimePicker";
import dayjs from "dayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

function Preferences() {
  //consts for the AI preferences
  const [alignment, setAlignment] = useState("android");
  const [alignment1, setAlignment1] = useState("solar");
  const [alignment2, setAlignment2] = useState("enabled");
  const [alignment3, setAlignment3] = useState("enable");

  const handleChange = (event, newAlignment) => {
    setAlignment(newAlignment);
  };
  const handleChange1 = (event, newAlignment1) => {
    setAlignment1(newAlignment1);
  };
  const handleChange2 = (event, newAlignment2) => {
    setAlignment2(newAlignment2);
  };
  const handleChange3 = (event, newAlignment3) => {
    setAlignment3(newAlignment3);
  };

  //consts for the user set preferences
  const [valueTime, setValueTime] = useState(dayjs("2014-08-18T21:11:54"));
  const [valueTime1, setValueTime1] = useState(dayjs("2014-08-18T21:11:54"));
  const handleChangeTime = (newValue) => {
    setValueTime(newValue);
  };
  const handleChangeTime1 = (newValue) => {
    setValueTime1(newValue);
  };

  const [values, setValues] = useState({
    amount: "",
    password: "",
    weight: "",
    weightRange: "",
    showPassword: false,
  });
  const [values1, setValues1] = useState({
    amount: "",
    password: "",
    weight: "",
    weightRange: "",
    showPassword: false,
  });
  const handleChangeAmount = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };
  const handleChangeAmount1 = (prop) => (event) => {
    setValues1({ ...values1, [prop]: event.target.value });
  };

  return (
    <>
      <Container fluid>
        <Row>
          <Col lg="3" sm="6">
            <Card className="card-stats">
              <Card.Body>
                <Row>
                  <Col xs="5">
                    <div className="icon-big text-center icon-warning">
                      <i className="nc-icon nc-chart text-warning"></i>
                    </div>
                  </Col>
                  <Col xs="7">
                    <div className="numbers">
                      <p className="card-category">Energy Produced</p>
                      <Card.Title as="h4">100W</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">In the last week</div>
              </Card.Footer>
            </Card>
          </Col>
          <Col lg="3" sm="6">
            <Card className="card-stats">
              <Card.Body>
                <Row>
                  <Col xs="5">
                    <div className="icon-big text-center icon-warning">
                      <i className="nc-icon nc-light-3 text-success"></i>
                    </div>
                  </Col>
                  <Col xs="7">
                    <div className="numbers">
                      <p className="card-category">Energy Used</p>
                      <Card.Title as="h4">200W</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">In the last week</div>
              </Card.Footer>
            </Card>
          </Col>
          <Col lg="3" sm="6">
            <Card className="card-stats">
              <Card.Body>
                <Row>
                  <Col xs="5">
                    <div className="icon-big text-center icon-warning">
                      <i className="nc-icon nc-vector text-danger"></i>
                    </div>
                  </Col>
                  <Col xs="7">
                    <div className="numbers">
                      <p className="card-category">Main Energy Source</p>
                      <Card.Title as="h4">Solar</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">In the last week</div>
              </Card.Footer>
            </Card>
          </Col>
          <Col lg="3" sm="6">
            <Card className="card-stats">
              <Card.Body>
                <Row>
                  <Col xs="5">
                    <div className="icon-big text-center icon-warning">
                      <i className="nc-icon nc-favourite-28 text-primary"></i>
                    </div>
                  </Col>
                  <Col xs="7">
                    <div className="numbers">
                      <p className="card-category">Money Saved</p>
                      <Card.Title as="h4">$238.97</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">In the last month</div>
              </Card.Footer>
            </Card>
          </Col>
        </Row>

        <Row>
          <Col md="6">
            <Card>
              <Card.Header>
                <Card.Title as="h4">User Set Preferences</Card.Title>
                <p className="card-category">Toggle to change</p>
              </Card.Header>
              <Card.Body>
                <div>
                  <h6>set auto-buy</h6>
                  <FormControl sx={{ m: 1 }} variant="filled">
                    <InputLabel htmlFor="filled-adornment-amount">
                      Amount
                    </InputLabel>
                    <FilledInput
                      id="filled-adornment-amount"
                      value={values.amount}
                      onChange={handleChangeAmount("amount")}
                      startAdornment={
                        <InputAdornment position="start">$</InputAdornment>
                      }
                    />
                  </FormControl>
                </div>
                <div style={{ marginTop: "10px" }}>
                  <h6>set auto-sell</h6>
                  <FormControl sx={{ m: 1 }} variant="filled">
                    <InputLabel htmlFor="filled-adornment-amount">
                      Amount
                    </InputLabel>
                    <FilledInput
                      id="filled-adornment-amount"
                      value={values1.amount}
                      onChange={handleChangeAmount1("amount")}
                      startAdornment={
                        <InputAdornment position="start">$</InputAdornment>
                      }
                    />
                  </FormControl>
                </div>
                <div style={{ marginTop: "10px" }}>
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <h6>time for battery top off</h6>
                    <TimePicker
                      value={valueTime}
                      onChange={handleChangeTime}
                      renderInput={(params) => <TextField {...params} />}
                    />
                  </LocalizationProvider>
                </div>
                <div style={{ marginTop: "10px" }}>
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <h6>time for car charging</h6>
                    <TimePicker
                      value={valueTime1}
                      onChange={handleChangeTime1}
                      renderInput={(params) => <TextField {...params} />}
                    />
                  </LocalizationProvider>
                </div>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">
                  <i className="fas fa-history mr-1"></i>
                  Updated 3 minutes ago
                </div>
              </Card.Footer>
            </Card>
          </Col>
          <Col md="6">
            <Card>
              <Card.Header>
                <Card.Title as="h4">AI Preferences</Card.Title>
                <p className="card-category">Toggle to change</p>
              </Card.Header>
              <Card.Body>
                <div>
                  <h6>Predict cloudiness and Extreme Weather</h6>
                  <ToggleButtonGroup
                    color="primary"
                    value={alignment2}
                    exclusive
                    onChange={handleChange2}
                    aria-label="Platform"
                  >
                    <ToggleButton value="enabled">Enabled</ToggleButton>
                    <ToggleButton value="disabled">Disabled</ToggleButton>
                  </ToggleButtonGroup>
                </div>
                <div>
                  <h6 style={{ marginTop: "10px" }}>predict car charging</h6>
                  <ToggleButtonGroup
                    color="primary"
                    value={alignment3}
                    exclusive
                    onChange={handleChange3}
                    aria-label="Platform"
                  >
                    <ToggleButton value="enable">Enabled</ToggleButton>
                    <ToggleButton value="disable">disabled</ToggleButton>
                  </ToggleButtonGroup>
                </div>
                <div>
                  <h6 style={{ marginTop: "10px" }}>Battery Refill Strategy</h6>
                  <ToggleButtonGroup
                    color="primary"
                    value={alignment}
                    exclusive
                    onChange={handleChange}
                    aria-label="Platform"
                  >
                    <ToggleButton value="web">Conservative</ToggleButton>
                    <ToggleButton value="android">Balanced</ToggleButton>
                    <ToggleButton value="ios">Aggressive</ToggleButton>
                  </ToggleButtonGroup>
                </div>
                <div style={{ marginTop: "10px" }}>
                  <h6>Energy Preference</h6>
                  <ToggleButtonGroup
                    color="primary"
                    value={alignment1}
                    exclusive
                    onChange={handleChange1}
                    aria-label="Platform"
                  >
                    <ToggleButton value="wind">Wind</ToggleButton>
                    <ToggleButton value="solar">Solar</ToggleButton>
                    <ToggleButton value="gas">Natural gas</ToggleButton>
                  </ToggleButtonGroup>
                </div>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className="stats">
                  <i className="fas fa-history mr-1"></i>
                  Updated 3 minutes ago
                </div>
              </Card.Footer>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md="4">
            <Card>
              <Card.Header>
                <Card.Title as="h4">Energy Consumption</Card.Title>
                <p className="card-category">Energy Source Breakdown</p>
              </Card.Header>
              <Card.Body>
                <div
                  className="ct-chart ct-perfect-fourth"
                  id="chartPreferences"
                >
                  <ChartistGraph
                    data={{
                      labels: ["40%", "20%", "40%"],
                      series: [40, 20, 40],
                    }}
                    type="Pie"
                  />
                </div>
                <div className="legend">
                  <i className="fas fa-circle text-info"></i>
                  Solar <i className="fas fa-circle text-danger"></i>
                  Natural Gas <i className="fas fa-circle text-warning"></i>
                  Wind
                </div>
                <hr></hr>
                <div className="stats">
                  <i className="far fa-clock mr-1"></i>
                  Last updated 7 days ago
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Preferences;
