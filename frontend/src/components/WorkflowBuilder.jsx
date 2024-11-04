// WorkflowBuilder.jsx
import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

function WorkflowBuilder() {
  const [workflow, setWorkflow] = useState([]);
  const [savedWorkflows, setSavedWorkflows] = useState([]);

  const addStep = (step) => setWorkflow([...workflow, step]);

  const saveWorkflow = () => {
    setSavedWorkflows([...savedWorkflows, workflow]);
    setWorkflow([]);
  };

  const onDragEnd = (result) => {
    if (!result.destination) return;
    const reorderedSteps = Array.from(workflow);
    const [removed] = reorderedSteps.splice(result.source.index, 1);
    reorderedSteps.splice(result.destination.index, 0, removed);
    setWorkflow(reorderedSteps);
  };

  return (
    <div>
      <h3>Create Your Workflow</h3>
      <DragDropContext onDragEnd={onDragEnd}>
        <Droppable droppableId="workflow">
          {(provided) => (
            <ul {...provided.droppableProps} ref={provided.innerRef}>
              {workflow.map((step, index) => (
                <Draggable key={step} draggableId={step} index={index}>
                  {(provided) => (
                    <li ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
                      {step}
                    </li>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </ul>
          )}
        </Droppable>
      </DragDropContext>
      <div>
        <button onClick={() => addStep('Select AI Model')}>Add AI Model Step</button>
        <button onClick={() => addStep('Set API Call')}>Add API Call Step</button>
      </div>
      <button onClick={saveWorkflow}>Save Workflow</button>
    </div>
  );
}

export default WorkflowBuilder;
