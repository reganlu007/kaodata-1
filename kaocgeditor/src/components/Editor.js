import React, {useState, useEffect} from 'react';
import getGameInfos from '../data/gameData.js';
import {fileToImageDataArray} from '../utils.js';
import '../styles/Editor.css';
import UploadImage from './UploadImage.js';
import {useDispatch, useSelector} from 'react-redux';
import {selectGame, modifyFace, clearModified} from '../reducers.js';
import PropTypes from 'prop-types';

function GameSelect(props) {
  const dispatch = useDispatch();
  const handleChange = (e) => {
    const gameId = e.target.value;
    props.setImageDataArray(null);
    dispatch(selectGame(gameId));
    props.setUploadBtnDisabled(false);
    dispatch(clearModified());
  };
  return (
    <select id="game-select" onChange={handleChange}>
      <option value="">--選擇遊戲--</option>
      {props.gameList.map((game) => (
        <option key={game.id} value={game.id}>
          {game.name}
        </option>
      ))}
    </select>
  );
}
GameSelect.propTypes = {
  gameList: PropTypes.arrayOf(
      PropTypes.shape({
        id: PropTypes.string.isRequired,
        name: PropTypes.string.isRequired,
      }),
  ).isRequired,
  setImageDataArray: PropTypes.func.isRequired,
  setUploadBtnDisabled: PropTypes.func.isRequired,
};

function ImageFigure(props) {
  const [imgUrl, setImgUrl] = useState(null);

  useEffect(() => {
    const canvas = document.createElement('canvas');
    canvas.width = props.imageData.width;
    canvas.height = props.imageData.height;
    const ctx = canvas.getContext('2d');
    ctx.putImageData(props.imageData, 0, 0);
    canvas.toBlob((blob) => {
      const url = URL.createObjectURL(blob);
      setImgUrl(url);
    });
  }, [props.imageData]);

  const faceIndex = props.imageKey + 1;

  const currentGame = useSelector((state) => state.editor.currentGame);
  const names = getGameInfos()[currentGame].names;
  const name =
    names[props.imageKey] === '' ? '(未命名)' : names[props.imageKey];

  console.log('Rendering ImageFigure');
  return (
    <figure
      id={`face-${props.imageKey + 1}`}
      className={`image-figure ${props.selected ? 'selected' : ''} ${
        props.modified ? 'modified' : ''
      }`}
      onClick={props.onClick}
    >
      {imgUrl && <img src={imgUrl} alt={`Image ${faceIndex}`} />}
      <figcaption>
        {faceIndex}
        <br />
        {name}
      </figcaption>
    </figure>
  );
}
ImageFigure.propTypes = {
  imageKey: PropTypes.number.isRequired,
  imageData: PropTypes.object.isRequired,
  selected: PropTypes.bool.isRequired,
  modified: PropTypes.bool.isRequired,
  onClick: PropTypes.func.isRequired,
};

function FaceList(props) {
  const dispatch = useDispatch();
  const [selectedIndex, setSelectedIndex] = useState(null);

  function handleFigureClick(e, index) {
    e.stopPropagation();
    if (selectedIndex === index) {
      setSelectedIndex(null);
    } else {
      setSelectedIndex(index);
    }
  }

  // This function is called when the user clicks the Apply button. It sets the
  // modified state for the selected index to true.
  const handleApplyClick = () => {
    dispatch(modifyFace(selectedIndex));
  };

  const handleSaveClick = () => {
    dispatch(clearModified());
    setSelectedIndex(null);
  };

  const modified = useSelector((state) => state.editor.modifiedFace);
  if (!props.imageDataArray) {
    return (
      <div className="image-list" id="image-list">
        請先選擇遊戲，並上傳檔案
      </div>
    );
  }
  return (
    <div className="image-list">
      <Apply disabled={selectedIndex === null} onClick={handleApplyClick} />
      <Save disabled={!modified.some((val) => val)} onClick={handleSaveClick} />
      <br />
      {props.imageDataArray.map((imageData, index) => (
        <ImageFigure
          key={index}
          imageKey={index}
          imageData={imageData}
          selected={selectedIndex == index}
          modified={modified[index]}
          onClick={(e) => handleFigureClick(e, index)}
        ></ImageFigure>
      ))}
    </div>
  );
}
FaceList.propTypes = {
  imageDataArray: PropTypes.arrayOf(PropTypes.object),
};

function Apply({disabled, onClick}) {
  return (
    <button className="apply-btn" disabled={disabled} onClick={onClick}>
      Apply
    </button>
  );
}
Apply.propTypes = {
  disabled: PropTypes.bool,
  onClick: PropTypes.func,
};

function Save({disabled, onClick}) {
  return (
    <button className="save-btn" disabled={disabled} onClick={onClick}>
      Save
    </button>
  );
}
Save.propTypes = {
  disabled: PropTypes.bool,
  onClick: PropTypes.func,
};

function Editor() {
  const [gameList, setGameList] = useState([]);
  const [UploadBtnDisabled, setUploadBtnDisabled] = useState(true);
  const [imageDataArray, setImageDataArray] = useState(() => null);

  useEffect(() => {
    // 從 gameData.js 文件中取得遊戲數據
    const gameInfos = getGameInfos();
    // 根據數據建立選項
    const list = Object.values(gameInfos).map((game) => ({
      id: game.id,
      name: game.name,
    }));
    setGameList(list);
  }, []);

  const handleFileSelected = (event) => {
    const gameSelect = document.querySelector('#game-select');
    const theGame = getGameInfos()[gameSelect.value];
    setImageDataArray(null);

    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onload = (event) => {
      const uint8Buffer = new Uint8Array(event.target.result);
      const imageDataArray = fileToImageDataArray(
          uint8Buffer,
          theGame.width,
          theGame.height,
          theGame.palette,
          theGame.halfHeight,
          theGame.count,
      );

      setImageDataArray(imageDataArray);
    };
  };

  return (
    <div className="container">
      <div className="settings">
        <GameSelect
          gameList={gameList}
          setImageDataArray={setImageDataArray}
          setUploadBtnDisabled={setUploadBtnDisabled}
        ></GameSelect>
        <input
          type="file"
          disabled={UploadBtnDisabled}
          onChange={handleFileSelected}
          //   accept="image/*"
        />
      </div>
      <div className="preview">
        <UploadImage></UploadImage> →<div className="result"></div>
        <button className="apply">Apply</button>
      </div>
      <hr />
      <FaceList imageDataArray={imageDataArray}></FaceList>
      <div className="clipboard">
        <h2>Clipboard</h2>
        <div className="image-grid"></div>
        <button className="copy">Copy</button>
        <button className="cut">Cut</button>
      </div>
    </div>
  );
}

export default Editor;
